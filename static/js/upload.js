$('#finput').on('change', function (e) {
    var reader = new FileReader()
    reader.onload = (e) =>{
        $("#tl_img").attr('src', e.target.result);
    }
    const a = reader.readAsDataURL(e.target.files[0]);
    return a
});

      // ドラッグしたままエリアに乗った＆外れたとき
      $(document).on('dragover', '#file_drag_drop_area, #file_drag_drop_area_stl', function (event) {
        event.preventDefault();
        $(this).css("background-color", "#999999");
    });
    $(document).on('dragleave', '#file_drag_drop_area, #file_drag_drop_area_stl', function (event) {
        event.preventDefault();
        $(this).css("background-color", "transparent");
    });

    // ドラッグした時
    $(document).on('drop', '#file_drag_drop_area', function (event) {
        let org_e = event;
        if (event.originalEvent) {
            org_e = event.originalEvent;
        }

        org_e.preventDefault();
        file_input.files = org_e.dataTransfer.files;
        console.log(file_input.files)
        var reader = new FileReader()
        reader.onload = (e) =>{
            $("#tl_img").attr('src', e.target.result);
        }
        const b = reader.readAsDataURL(file_input.files[0]);
        $(this).css("background-color", "transparent");
        return b
    });                                                                                                                                                                        