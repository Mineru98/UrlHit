'use strict';
if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
    $('body').append(`<div class="top nav">
    <ul>
        <li>
            <a class="active" style="padding-top:8px;padding-bottom:8px;padding-left:16px;padding-right:0px;height:48px;" href="/">
                <img src="static/imgs/punch.png" width="32">
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
<div class="content top">
    <h1 class="ui header">Apply</h1>
</div>

<div class="content mid">
    <div class="ui tiny modal">
        <i class="close icon"></i>
        <div class="header">
            Tag 추가
        </div>
        <div class="image content">
            <div class="description">
                <div class="ui action fluid right input">
                    <input type="text" class="normal" id="tag-input" placeholder="input new tag">
                </div>
            </div>
        </div>
        <div class="actions">
            <div class="ui deny button" id="cancel">
                취소
            </div>
            <div class="ui positive right icon button" id="add">
                추가
            </div>
        </div>
    </div>
    <div class="ui text container segment">
        <h2 class="ui header">Url Apply</h2>
        <p>원하는 URL을 등록하고 해당 링크로 연결하세요.</p>
        <p></p>
    </div>
    <div class="ui one column center aligned grid">
        <div class="row">
            <div class="column">
                <div class="ui action right labeled input first">
                    <input type="text" class="large" id="search-url" placeholder="input your site">
                    <div class="ui blue button" id="search">Search</div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="column tag-list">
            </div>
        </div>
        <div class="row">
            <div class="column">
                <div class="ui action right labeled input second transition hidden">
                    <input type="text" class="normal" id="apply-url" placeholder="Find domain" readonly>
                    <div class="ui blue button" id="apply">Apply</div>
                </div>
            </div>
        </div>
    </div>
</div>

`);
} else {
    $('body').append(`
<div class="ui overlay visible left vertical inverted sidebar menu default">
    <div class="menu top">
        <img src="{{ url_for('static', filename='imgs/punch.png') }}" width="64">
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
    <div class="content top">
        <h1 class="ui header">Apply</h1>
    </div>

    <div class="content mid">
        <div class="ui tiny modal">
            <i class="close icon"></i>
            <div class="header">
                Tag 추가
            </div>
            <div class="image content">
                <div class="description">
                    <div class="ui action fluid right input">
                        <input type="text" class="normal" id="tag-input" placeholder="input new tag">
                    </div>
                </div>
            </div>
            <div class="actions">
                <div class="ui deny button" id="cancel">
                    취소
                </div>
                <div class="ui positive right icon button" id="add">
                    추가
                </div>
            </div>
        </div>
        <div class="ui text container segment">
            <h2 class="ui header">Url Apply</h2>
            <p>원하는 URL을 등록하고 해당 링크로 연결하세요.</p>
            <p></p>
        </div>
        <div class="ui one column center aligned grid">
            <div class="row">
                <div class="column">
                    <div class="ui action right labeled input first">
                        <input type="text" class="large" id="search-url" placeholder="input your site">
                        <div class="ui blue button" id="search">Search</div>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="column tag-list">
                </div>
            </div>
            <div class="row">
                <div class="column">
                    <div class="ui action right labeled input second transition hidden">
                        <input type="text" class="normal" id="apply-url" placeholder="Find domain" readonly>
                        <div class="ui blue button" id="apply">Apply</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>`);
}