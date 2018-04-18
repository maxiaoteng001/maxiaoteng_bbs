var log = function() {
    console.log.apply(console, arguments)
}

var e = function(sel) {
    return document.querySelector(sel)
}

var timeString = function(timestamp) {
    t = new Date(timestamp * 1000)
    t = t.toLocaleString('ja-JP')
    return t
}

var test= function(){
    alert('测试')
}

/*
 ajax 函数
*/
var ajax = function(method, path, data, responseCallback) {
    var r = new XMLHttpRequest()
    // 设置请求方法和请求地址
    r.open(method, path, true)
    // 设置发送的数据的格式为 application/json
    // 这个不是必须的
    r.setRequestHeader('Content-Type', 'application/json')
    // 注册响应函数
    r.onreadystatechange = function() {
        if(r.readyState === 4) {
            // r.response 存的就是服务器发过来的放在 HTTP BODY 中的数据
            responseCallback(r.response)
        }
    }
    // 把数据转换为 json 格式字符串
    data = JSON.stringify(data)
    // 发送请求
    r.send(data)
}

// 删除一个 Board
var apiBoardDelete = function(id, callback) {
    var path = '/admin/delete_board/' + id
    ajax('GET', path, '', callback)
    //    get(path, callback)
}
