
//获取cookie
function get_cookie(name) {
    var xsrf_cookies = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return xsrf_cookies[1]
}


//提交登录请求
$(document).ready(function(){
    $('#submit_login').click(function () {
        event.preventDefault();
        var remember = '';
        $.each($('input:checkbox'),function(){
            if(this.checked){
                remember = $(this).val();
            }else{
                remember = '';
            }
        });
        $.ajax({
            'url': '/auth/user_login',
            'type': 'post',
            'data': {
               'name': $('#name').val(),
               'password':  $('#password').val(),
               'code':  $('#code').val(),
               'captcha':  $('#captcha').val(),
            },
            'headers':{
                 "X-XSRFTOKEN":get_cookie("_xsrf")
            },
            'success': function (data) {
               if(data['status'] == 200){
                   swal({
                    'title': '正确',
                    'text': data['msg'],
                    'type': 'success',
                    'showCancelButton': false,
                    'showConfirmButton': false,
                    'timer': 1500,
                    'closeOnConfirm': false
                    },function () {
                       window.location = '/account/user_profile';
                    });
               }else {
                    swal({
                    'title': '错误111111',
                    'text': data['msg'],
                    'type': 'error',
                    'showCancelButton': false,
                    'showConfirmButton': false,
                    'timer': 1500
                    });
                    get_image_code();
               }
            }
        });
    });
});

