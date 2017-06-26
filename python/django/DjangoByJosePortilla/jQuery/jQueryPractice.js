// $('h1').click(function() {
  // Instead of typing in the item again, you can refer to it
  // as this.
  // $(this).text('I was changed!');

  // Instead of doing the following. Even though it's currently the same
  // length, there are probably many times just referring to "this" would
  // be more efficient.
  // $('h1').text('Was I changed?');
// });

// KEY PRESS
// $('input').eq(0).keypress(function() {
//   $('h3').toggleClass('turnBlue');
// });

// $('input').eq(0).keypress(function(event) {
//   if (event.which === 13) {
//     $('h3').toggleClass('turnBlue');
//   }
// })

// on method
// $('h1').on('dblclick', function() {
//   $(this).toggleClass('turnBlue');
// })


// This is a cool example I found on the internet when
// figuring out how to toggle test.
// jQuery.fn.extend({
//     toggleText: function (a, b){
//         var that = this;
//             if (that.text() != a && that.text() != b){
//                 that.text(a);
//             }
//             else
//             if (that.text() == a){
//                 that.text(b);
//             }
//             else
//             if (that.text() == b){
//                 that.text(a);
//             }
//         return this;
//     }
// });

// MOUSEOVER FUNCTION
// $('h1').on('mouseover', function() {
//   $(this).toggleClass('turnBlue');
//   $(this).toggleText('This is before!', 'Now after!!!')
// })




// ANIMATION
$('input').eq(1).on('click', function() {
  // fadeOut example
  // $('.container').fadeOut(3000);

  // slideUp example
  $('.container').slideUp(1000);
})
