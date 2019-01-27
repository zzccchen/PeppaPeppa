window.onload = function () {
    var x = document.getElementById("code_img");
    $.get('/api/ocr', {
        address: x.src
    }, function (response) {
        console.log(response);
        document.getElementById('verify').value = response.data.ocr_data;
    });
};