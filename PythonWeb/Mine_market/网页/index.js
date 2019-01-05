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
        // 下拉菜单，添加点击时间，传值显示
        $(".select li").each(function () {
           $(this).click(function () {
               $('.currentAddress').html($(this).html());
           })
        });



        // 图片轮播
        var imgIndex = 0;
        var timerId = setInterval(autoPlay,1000);
        function autoPlay() {
            var $imgs = $('#banner img');
            $imgs.each(function () {
                    $(this).css('display','none');
                });
            imgIndex = ++imgIndex === $imgs.length ? 0 : imgIndex++;
            // 根据下标去元素;
            $imgs.eq(imgIndex).css('display','block');

            // 图标
            var $li = $('#banner li');
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
    });