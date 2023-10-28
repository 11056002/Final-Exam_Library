$(document).ready(function () {
    // 在文档准备就绪时，绑定MENU选项的点击事件
    $(".list-group-item").click(function () {
        // 获取选择的MENU文本
        var selectedMenu = $(this).text().trim();

        // 使用AJAX请求更新文章列表
        $.ajax({
            type: "GET",
            url: "/api/" + selectedMenu + "/",  // 这里需要与Django视图的URL匹配
            dataType: "json",
            success: function (data) {
                $("#article-list").empty();
                if (selectedMenu === "書本") {
                    // 显示书本的文章列表
                    data.forEach(function (item) {
                        var bookHTML = `<div class="card">`;
                        // 创建书本内容的HTML并插入文章列表
                        // ...
                        bookHTML += `</div>`;
                        $("#article-list").append(bookHTML);
                    });
                } else if (selectedMenu === "作者") {
                    // 类似书本，根据数据创建作者内容的HTML并插入文章列表
                } else if (selectedMenu === "出版商") {
                    // 类似书本，根据数据创建出版商内容的HTML并插入文章列表
                }
            }
        });
    });
});
