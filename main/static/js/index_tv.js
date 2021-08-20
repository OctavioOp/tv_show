$(document).ready(function () {
  
  
  $('.delete').on('click', function (e) {
    e.prevenDefault()
    swal({
      title: 'Are you sure?',
      text: 'you will lost the info forever',
      icon: 'warning',
      buttons: true,
      dangerMode: true
    }).then((willdelete)=>{
      if(willdelete){
        swal({
          title: 'Poof! your kill your data',
          icon: 'success'
        })
      }
      else{
        swal({
          title: 'uff! your data is safe',
        })

      }
    })
  })

  
})