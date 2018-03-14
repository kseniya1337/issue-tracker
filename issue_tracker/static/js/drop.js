// $('.dashboard .col-3').sortable({
//     stop: function (e, ui) {
//         console.log('stop', e, ui)
//
//         console.log($(ui.item).data('id'));
//
//         $.ajax({
//             url: '/api/change_position',
//             data: {
//                 issue_id: $(ui.item).data('id'),
//                 status: $(ui.item).closest('.column.col-3').data('status')
//             },
//             method: 'post',
//             success: function (response) {
//                 console.log(response);
//             }
//         })
//     },
//     connectWith: '.dashboard .col-3'
// });