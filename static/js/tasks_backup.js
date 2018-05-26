$(function () {

  $(".js-create-task").click(function () {
    $.ajax({
      url: '/tasks/create/',
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-task").modal("show");
      },
      success: function (data) {
        console.log(data)
        $("#modal-task .modal-content").html(data.html_form);
      }
    });
  });

});


$("#modal-task").on("submit", ".js-task-create-form", function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        console.log(data)
        if (data.form_is_valid) {
          alert("Book created!");
          $("#task-table tbody").html(data.html_task_list);  // <-- Replace the table body
          $("#modal-task").modal("hide");  // <-- Close the modal
        }
        else {
          $("#modal-task .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  });
