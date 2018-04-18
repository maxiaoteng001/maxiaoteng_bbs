


/*//var doComplete = function(id){
//    var url = "/complete/"+id
//    log(url)
//    $.get(url)
//}
*/

var bindEventBoardDelete = function() {
    var todo_table = e('.todo-table')
    // 注意, 第二个参数可以直接给出定义函数
    todo_table.addEventListener('click', function(event){
        var self = event.target
//        log('点击对象:', self)
        if(self.classList.contains('delete-btn')){
            var tr = self.parentElement.parentElement
            var id = tr.dataset.id
            log(id)
            if(id>0){
                apiBoardDelete(id, function(r) {
                    var return_t = JSON.parse(r)
                    if(return_t.id==id){
                        tr.remove()
                    }
                    else{
                        alert('没有权限')
                    }
                })
            }
        }
    })
}

var bindEvents = function() {
//    使用jquery发送get请求
//    doComplete()
//    使用ajax发送get请求
//    bindEventTodoComplete()
    bindEventBoardDelete()

}


var __main = function() {
    bindEvents()
//    loadTodos()
}

__main()
