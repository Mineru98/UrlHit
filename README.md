# UrlHit
[GoogleDrive](https://script.google.com/macros/s/AKfycbzrmd2D4AnEa6LIZiUtOE64ybyyok_zaQYnXq8mfvcTR6CBFQ/exec)
```
$.ajax({
    type: "GET",
    url: "https://script.google.com/macros/s/AKfycbzrmd2D4AnEa6LIZiUtOE64ybyyok_zaQYnXq8mfvcTR6CBFQ/exec",
    data: {
      "Type": inputName.val(),
      "Url": inputAge.val(),
      "Time": inputArea.val()
    },
    success: function (response) {
      isLoading(false);

      snackbar.html('입력이 완료됐습니다.').addClass('show');
      setTimeout(function () {
        snackbar.removeClass('show');
      }, 3000);

      //값 비워주기
      inputName.val('');
      inputAge.val('');
      inputArea.val('');
    },
    error: function (request, status, error) {
      isLoading(false);
      console.log("code:" + request.status + "\n" + "error:" + error);
      console.log(request.responseText);
    }
  });
```

Version 0.0.1

```
pip install flask
```
