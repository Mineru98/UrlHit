'use strict';
if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
    $('body').append(`<div class="top nav">
    <ul>
        <li>
            <a class="active" style="padding-top:8px;padding-bottom:8px;padding-left:16px;padding-right:0px;height:48px;" href="/">
                <img src="http://www.urlhit.shop/static/imgs/punch.png" width="32">
            </a>
        </li>
        <li>
            <a class="active" href="/">UrlHit</a>
        </li>
        <li>
            <a href="/apply">Apply</a>
        </li>
        <li>
            <li style="float:right">
                <a href="#">Sign In</a>
            </li>
        </li>
        <li>
            <li style="float:right">
                <a href="#">Sign Up</a>
            </li>
        </li>
    </ul>
</div>
<div class="content mid">
    <h2>요청하신 페이지는 존재하지 않습니다.</h2>
</div>

`);
} else {
    $('body').append(`
<div class="ui overlay visible left vertical inverted sidebar menu default">
    <div class="menu top">
        <img src="http://www.urlhit.shop/static/imgs/punch.png" width="64">
    </div>
    <div class="menu top">
        <h3 class="ui header white">UrlHit</h3>
    </div>
    <a class="item" href="/">
        <div class="ui header white">
            <i class="home icon size-a">
            </i>
            Home
        </div>
    </a>
    <a class="item" href="/apply">
        <div class="ui header white">
            <i class="edit icon size-a">
            </i>
            Apply
        </div>
    </a>
</div>
<div class="pusher">
    <div class="content mid">
        <h1>요청하신 페이지는 존재하지 않습니다.</h1>
    </div>
</div>`);
}