$(function() {
    $('.drop_element').draggable({
    });
    $('#block2').droppable({
        hoverClass: 'dropHere'
        ,drop: function(event, ui) {
            $(this).append($('<div class="textBlock">' + ui.draggable.html() + '</div>'));
        }
    });
});