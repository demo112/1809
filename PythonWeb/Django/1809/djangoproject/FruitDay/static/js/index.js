// 获取图片数组
// 开启定时器，切换下标获取图片，空值隐藏于显示
// window.onload = function () {
//     var imgIndex = 0;
//     var imgs = document.getElementsById('banner').child;
//     setInterval(function () {
//         // 越界判断
//         imgIndex++;
//         imgs[imgIndex].style.display = block;
//         imgs[imgIndex].siblings().style.display = none;
//     },1000);
//
//     $('#banner img');
// };


$(function () {
    //调用检车用户登陆信息的方法
    check_login();
    loadGoods();
    // 下拉菜单，添加点击时间，传值显示
    $(".select li").each(function () {
       $(this).click(function () {
           $('.currentAddress').html($(this).html());
       })
    });

    // 图片轮播
    let imgIndex = 0;
    let timerId = setInterval(autoPlay,1000);
    function autoPlay() {
        let $imgs = $('#banner img');
        $imgs.each(function () {
                $(this).css('display','none');
            });
        imgIndex = ++imgIndex === $imgs.length ? 0 : imgIndex++;
        // 根据下标去元素;
        $imgs.eq(imgIndex).css('display','block');

        // 图标
        let $li = $('#banner li');
        $li.each(function () {
            $(this).css('background','#64a131');
        });
        $li.eq(imgIndex).css('background','red');
    }
    $('#banner').bind("mouseover", function () {
        clearInterval(timerId);
        $('#banner img').each(function () {
            $(this).removeAttr('display');
        })
    }).mouseout(function () {
        // 鼠标移出，重启定时器
        timerId = setInterval(autoPlay,1000);
    })
    // 加载所有的商品类型以及商品信息


});


function createXhr() {
    let xhr = null;
    if (window.XMLHttpRequest) {
        xhr = new XMLHttpRequest()
    } else {
        xhr = new ActiveXObject('Microsoft.XMLHTTP');
    }
    return xhr
}


// function check_pwd1() {
//     //创建xhr对象
//     let xhr = createXhr();
//     //创建请求
//     xhr.open('get', '/checkrepeat_email', true);
//     //设置回调函数
//     xhr.onreadystatechange = function () {
//         if (xhr.readyState === 4 && xhr.status === 200) {
//             document.getElementById('check_eml').innerHTML=xhr.responseText;
//         }
//     };
//     //发送请求
//     xhr.send(null);
// }

//注册——检查信息是否重复
// function check_name(name) {
//     let xhr = createXhr();
//     let input = document.getElementsByName(name)[0].value;
//     xhr.open('get', '/check?' + name + '=' + input + '&tag=' + name, true);
//     console.log(name, input);
//     xhr.onreadystatechange = function () {
//         let rep = null;
//         if (name === 'uemail') {
//             if (xhr.readyState === 4 && xhr.status === 200) {
//                 rep = xhr.responseText;
//                 document.getElementById("check_email").innerHTML = rep;
//             } else {
//                 rep = "email异常";
//                 document.getElementById("check_email").innerHTML = rep;
//             }
//         } else if (name === 'nickname') {
//             if (xhr.readyState === 4 && xhr.status === 200) {
//                 rep = xhr.responseText;
//                 document.getElementById("check_nickname").innerHTML = rep;
//             } else {
//                 rep = "nickname异常";
//                 document.getElementById("check_nickname").innerHTML = rep;
//             }
//         }else if (name === 'uphone') {
//             if (xhr.readyState === 4 && xhr.status === 200) {
//                 rep = xhr.responseText;
//                 document.getElementById("check_phone").innerHTML = rep;
//             } else {
//                 rep = "phone异常";
//                 document.getElementById("check_phone").innerHTML = rep;
//             }
//         }
//     };
//     xhr.send(null)
// }


$(function () {
   $('#upwd2').blur(function () {
       console.log($(this).val());
   })
});


//注册——检查手机号是否重复
function btn_check_phone() {
    var params = {
        'uphone': $('[name=uphone]').val()
    };
    console.log(params);

    $.get('/check_uphone/', params, function (data) {
       $('#check_phone').html(data)
    });
}


//主页——检查当前页面是否登陆
function check_login() {
    $.get('/check_login/', function (data) {
        var html = '';
        if (data.login_status === 0) {
            html += "<a href='/login'>[ 登 陆 ]<a>";
            html += "<a href='/signup'>[ 注 册 ]<a>";
        }else {
            html += '欢迎' + data.uname;
            html += "<a href='/logout'>[ 登 出 ]<a>";
        }
        // 将html显示在指定的位置处
        $('#login').html(html);
    }, 'json');
}

function loadGoods() {
    $.get('/type_goods/', function (data) {
        var html = '';
        $.each(data, function (i, obj) {
            html += "<div class='goodsType'>";
            var jsonType = JSON.parse(obj.type);
            console.log(jsonType);
            html += '<p class="goodsTitle">' +
                    '    <img src="/' + jsonType.picture + '" alt="t4未加载">' +
                    '    <a href="">更多</a>\n' +
                    '</p>';
            html += '<ul>';
            var jsonGoods = JSON.parse(obj.goods);
            console.log(jsonGoods);
            $.each(jsonGoods, function (j, good) {
                html += '<li';
                if ((j+1) % 5 === 0) {
                html += 'class="no_margin"'
                }

                html += '>';
                html += '<div>';
                    html += "<img src='/" + good.fields.picture + "'>";
                html += '</div>';
                html += "<a href='#'>";
                    html += "<img src='../static/images/cart.png'>";
                html += "</a>";
                html += '</li>';
            });
            html += '</ul>';
            html += '<div>'
        });
        $('#main').html(html);
        console.log(data)
    }, 'json')
}
