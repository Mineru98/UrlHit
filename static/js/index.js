'use strict';
if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
    $('body').append(`
<style>
    canvas {
        -moz-user-select: none;
        -webkit-user-select: none;
        -ms-user-select: none;
    }

    .chart-container {
        width: 100%;
        margin-top: 40px;
        margin-bottom: 40px;
    }

    .container {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: center;
    }
</style>
<div class="top nav">
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
<div class="pusher mobile">
    <div class="content top mobile">
        <h1 class="ui header">Home</h1>
    </div>
    <div class="content mid mobile">
        <div class="container">
        </div>
        <script>
            const colorSet = ["#cd6155", "#af7ac5", "#5499c7", "#48c9b0", "#52be80", "#f4d03f", "#eb984e", "#f0f3f4", "#aab7b8", "#5d6d7e", "#ec7063", "#a569bd", "#5dade2", "#45b39d", "#58d68d", "#f5b041", "#dc7633", "#cacfd2", "#99a3a4", "#566573", "#d98880", "#c39bd3", "#7fb3d5", "#76d7c4", "#7dcea0", "#f7dc6f", "#f0b27a", "#f4f6f7", "#bfc9ca", "#85929e", "#f1948a", "#bb8fce", "#85c1e9", "#73c6b6", "#82e0aa", "#f8c471", "#e59866", "#d7dbdd", "#b2babb", "#808b96", "#e6b0aa", "#d7bde2", "#a9cce3", "#a3e4d7", "#a9dfbf", "#f9e79f", "#f5cba7", "#f7f9f9", "#d5dbdb", "#aeb6bf", "#f5b7b1", "#d2b4de", "#aed6f1", "#a2d9ce", "#abebc6", "#fad7a0", "#edbb99", "#e5e7e9", "#ccd1d1", "#abb2b9", "#f2d7d5", "#ebdef0", "#d4e6f1", "#d1f2eb", "#d4efdf", "#fcf3cf", "#fae5d3", "#fbfcfc", "#eaeded", "#d6dbdf", "#fadbd8", "#e8daef", "#d6eaf8", "#d0ece7", "#d5f5e3", "#fdebd0", "#f6ddcc", "#f2f3f4", "#e5e8e8", "#d5d8dc", "#f9ebea", "#f5eef8", "#eaf2f8", "#e8f8f5", "#e9f7ef", "#fef9e7", "#fdf2e9", "#fdfefe", "#f4f6f6", "#ebedef", "#fdedec", "#f4ecf7", "#ebf5fb", "#e8f6f3", "#eafaf1", "#fef5e7", "#fbeee6", "#f8f9f9", "#f2f4f4", "#eaecee", "#641e16", "#512e5f", "#154360", "#0e6251", "#145a32", "#7d6608", "#784212", "#7b7d7d", "#4d5656", "#1b2631", "#78281f", "#4a235a", "#1b4f72", "#0b5345", "#186a3b", "#7e5109", "#6e2c00", "#626567", "#424949", "#17202a", "#7b241c", "#633974", "#1a5276", "#117864", "#196f3d", "#9a7d0a", "#935116", "#979a9a", "#5f6a6a", "#212f3c", "#943126", "#5b2c6f", "#21618c", "#0e6655", "#1d8348", "#9c640c", "#873600", "#797d7f", "#515a5a", "#1c2833", "#922b21", "#76448a", "#1f618d", "#148f77", "#1e8449", "#b7950b", "#af601a", "#b3b6b7", "#717d7e", "#283747", "#b03a2e", "#6c3483", "#2874a6", "#117a65", "#239b56", "#b9770e", "#a04000", "#909497", "#616a6b", "#212f3d", "#a93226", "#884ea0", "#2471a3", "#17a589", "#229954", "#d4ac0d", "#ca6f1e", "#d0d3d4", "#839192", "#2e4053", "#cb4335", "#7d3c98", "#2e86c1", "#138d75", "#28b463", "#d68910", "#ba4a00", "#a6acaf", "#707b7c", "#273746", "#c0392b", "#9b59b6", "#2980b9", "#1abc9c", "#27ae60", "#f1c40f", "#e67e22", "#ecf0f1", "#95a5a6", "#34495e", "#e74c3c", "#8e44ad", "#3498db", "#16a085", "#2ecc71", "#f39c12", "#d35400", "#bdc3c7", "#7f8c8d", "#2c3e50"];

            function CirclePieConfig(labels, data) {
                const _colorSet = [];
                for (var i = 0; i < labels.length; i++)
                    _colorSet.push(colorSet[parseInt(Math.random() * 200) + 1]);
                return {
                    type: "pie",
                    data: {
                        labels: labels,
                        datasets: [{
                            label: '',
                            data: data,
                            backgroundColor: _colorSet,
                            borderWidth: 1,
                            pointStyle: 'rectRot',
                            pointRadius: 5,
                            pointBorderColor: 'rgb(0, 0, 0)'
                        }]
                    },
                    options: {
                        responsive: true,
                        legend: {
                            labels: {
                                usePointStyle: false
                            }
                        },
                        scales: {
                            x: {
                                display: true,
                                scaleLabel: {
                                    display: true,
                                }
                            },
                            y: {
                                display: true,
                                scaleLabel: {
                                    display: true,
                                }
                            }
                        },
                        title: {
                            display: true,
                        }
                    }
                };
            };

            function createPointStyleConfig(title, labels, data) {
                var config;
                config = CirclePieConfig(labels, data);
                config.options.legend.labels.usePointStyle = true;
                config.options.title.text = title;
                return config;
            };
            window.onload = function() {
                const _data = [];
                const labelList = [];
                const dataList = [];
                const shortUrlList = [];
                $.ajax({
                    type: "POST",
                    url: "/",
                    dataType: "json",
                    contentType: "application/json",
                    data: JSON.stringify(_data),
                    success: function(result) {
                        var canvasList = [];
                        for (var i = 1; i <= result.urlCount; i++)
                            $(".container").append('<div class="chart-container"><canvas id="canvas' + i + '"></canvas></div>');
                        if (result.Code == 200) {
                            for (var i = 1; i <= result.urlCount; i++) {
                                shortUrlList.push(Object.values(result.urls[i].shortulrs));
                                labelList.push(Object.keys(result.urls[i].tags));
                                dataList.push(Object.values(result.urls[i].tags));
                                canvasList.push({
                                    id: 'canvas' + i,
                                    config: createPointStyleConfig(result.urls[i].url, labelList[i - 1], dataList[i - 1])
                                })
                            }
                        }
                        canvasList.forEach(function(details) {
                            var ctx = document.getElementById(details.id).getContext('2d');
                            new Chart(ctx, details.config);
                        });
                    },
                    error: function(xhr, status, error) {
                        console.log(error);
                    }
                });
            };
        </script>
    </div>
</div>`);
} else {
    $('body').append(`
<style>
    canvas {
        -moz-user-select: none;
        -webkit-user-select: none;
        -ms-user-select: none;
    }

    .chart-container {
        width: 500px;
        margin-top: 40px;
        margin-bottom: 40px;
    }

    .container {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: center;
    }
</style>
<div class="ui overlay visible left vertical inverted sidebar menu default">
    <div class="menu top">
        <img src="static/imgs/punch.png" width="64">
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
        <h1 class="ui header">Home</h1>
    </div>
    <div class="content mid">
        <div class="container">
        </div>
        <script>
            const colorSet = ["#cd6155", "#af7ac5", "#5499c7", "#48c9b0", "#52be80", "#f4d03f", "#eb984e", "#f0f3f4", "#aab7b8", "#5d6d7e", "#ec7063", "#a569bd", "#5dade2", "#45b39d", "#58d68d", "#f5b041", "#dc7633", "#cacfd2", "#99a3a4", "#566573", "#d98880", "#c39bd3", "#7fb3d5", "#76d7c4", "#7dcea0", "#f7dc6f", "#f0b27a", "#f4f6f7", "#bfc9ca", "#85929e", "#f1948a", "#bb8fce", "#85c1e9", "#73c6b6", "#82e0aa", "#f8c471", "#e59866", "#d7dbdd", "#b2babb", "#808b96", "#e6b0aa", "#d7bde2", "#a9cce3", "#a3e4d7", "#a9dfbf", "#f9e79f", "#f5cba7", "#f7f9f9", "#d5dbdb", "#aeb6bf", "#f5b7b1", "#d2b4de", "#aed6f1", "#a2d9ce", "#abebc6", "#fad7a0", "#edbb99", "#e5e7e9", "#ccd1d1", "#abb2b9", "#f2d7d5", "#ebdef0", "#d4e6f1", "#d1f2eb", "#d4efdf", "#fcf3cf", "#fae5d3", "#fbfcfc", "#eaeded", "#d6dbdf", "#fadbd8", "#e8daef", "#d6eaf8", "#d0ece7", "#d5f5e3", "#fdebd0", "#f6ddcc", "#f2f3f4", "#e5e8e8", "#d5d8dc", "#f9ebea", "#f5eef8", "#eaf2f8", "#e8f8f5", "#e9f7ef", "#fef9e7", "#fdf2e9", "#fdfefe", "#f4f6f6", "#ebedef", "#fdedec", "#f4ecf7", "#ebf5fb", "#e8f6f3", "#eafaf1", "#fef5e7", "#fbeee6", "#f8f9f9", "#f2f4f4", "#eaecee", "#641e16", "#512e5f", "#154360", "#0e6251", "#145a32", "#7d6608", "#784212", "#7b7d7d", "#4d5656", "#1b2631", "#78281f", "#4a235a", "#1b4f72", "#0b5345", "#186a3b", "#7e5109", "#6e2c00", "#626567", "#424949", "#17202a", "#7b241c", "#633974", "#1a5276", "#117864", "#196f3d", "#9a7d0a", "#935116", "#979a9a", "#5f6a6a", "#212f3c", "#943126", "#5b2c6f", "#21618c", "#0e6655", "#1d8348", "#9c640c", "#873600", "#797d7f", "#515a5a", "#1c2833", "#922b21", "#76448a", "#1f618d", "#148f77", "#1e8449", "#b7950b", "#af601a", "#b3b6b7", "#717d7e", "#283747", "#b03a2e", "#6c3483", "#2874a6", "#117a65", "#239b56", "#b9770e", "#a04000", "#909497", "#616a6b", "#212f3d", "#a93226", "#884ea0", "#2471a3", "#17a589", "#229954", "#d4ac0d", "#ca6f1e", "#d0d3d4", "#839192", "#2e4053", "#cb4335", "#7d3c98", "#2e86c1", "#138d75", "#28b463", "#d68910", "#ba4a00", "#a6acaf", "#707b7c", "#273746", "#c0392b", "#9b59b6", "#2980b9", "#1abc9c", "#27ae60", "#f1c40f", "#e67e22", "#ecf0f1", "#95a5a6", "#34495e", "#e74c3c", "#8e44ad", "#3498db", "#16a085", "#2ecc71", "#f39c12", "#d35400", "#bdc3c7", "#7f8c8d", "#2c3e50"];

            function CirclePieConfig(labels, data) {
                const _colorSet = [];
                for (var i = 0; i < labels.length; i++)
                    _colorSet.push(colorSet[parseInt(Math.random() * 200) + 1]);
                return {
                    type: "pie",
                    data: {
                        labels: labels,
                        datasets: [{
                            label: '',
                            data: data,
                            backgroundColor: _colorSet,
                            borderWidth: 1,
                            pointStyle: 'rectRot',
                            pointRadius: 5,
                            pointBorderColor: 'rgb(0, 0, 0)'
                        }]
                    },
                    options: {
                        responsive: true,
                        legend: {
                            labels: {
                                usePointStyle: false
                            }
                        },
                        scales: {
                            x: {
                                display: true,
                                scaleLabel: {
                                    display: true,
                                }
                            },
                            y: {
                                display: true,
                                scaleLabel: {
                                    display: true,
                                }
                            }
                        },
                        title: {
                            display: true,
                        }
                    }
                };
            };

            function createPointStyleConfig(title, labels, data) {
                var config;
                config = CirclePieConfig(labels, data);
                config.options.legend.labels.usePointStyle = true;
                config.options.title.text = title;
                return config;
            };
            window.onload = function() {
                const _data = [];
                const labelList = [];
                const dataList = [];
                const shortUrlList = [];
                $.ajax({
                    type: "POST",
                    url: "/",
                    dataType: "json",
                    contentType: "application/json",
                    data: JSON.stringify(_data),
                    success: function(result) {
                        var canvasList = [];
                        for (var i = 1; i <= result.urlCount; i++)
                            $(".container").append('<div class="chart-container"><canvas id="canvas' + i + '"></canvas></div>');
                        if (result.Code == 200) {
                            for (var i = 1; i <= result.urlCount; i++) {
                                shortUrlList.push(Object.values(result.urls[i].shortulrs));
                                labelList.push(Object.keys(result.urls[i].tags));
                                dataList.push(Object.values(result.urls[i].tags));
                                canvasList.push({
                                    id: 'canvas' + i,
                                    config: createPointStyleConfig(result.urls[i].url, labelList[i - 1], dataList[i - 1])
                                })
                            }
                        }
                        canvasList.forEach(function(details) {
                            var ctx = document.getElementById(details.id).getContext('2d');
                            new Chart(ctx, details.config);
                        });
                    },
                    error: function(xhr, status, error) {
                        console.log(error);
                    }
                });
            };
        </script>
    </div>
</div>`);
}