$('#finput').on('change', function () {
    var file = $(this).prop('files')[0];
    $('#foutput').text(file.name);
});