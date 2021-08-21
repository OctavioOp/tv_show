$(document).ready(function () {


  $('.delete').on('click', function (e) {

    e.preventDefault()
    id_delete = $('.delete').val()
    swal({
      title: 'Are you sure?',
      text: 'you will lost the info forever',
      icon: 'warning',
      buttons: true,
      dangerMode: true
    }).then((willdelete) => {
      if (willdelete) {
        swal({
          title: 'Poof! your kill your data',
          icon: 'success'
        })
        $.ajax({
          url: `../home/delete_by_ajax/${id_delete}`,
          method: 'POST'

        })
      }
      else {
        swal({
          title: 'uff! your data is safe',
        })

      }
    })
  })

})