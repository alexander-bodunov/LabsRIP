/**
 * Created by Work on 09.12.2016.
 */
$(window).load(onLoad())
function onLoad() {

}


/*.keypress ( function (e) {
    e. preventDefault ();
    //alert ($to -  $from ,'hghghghghgh');
    console.log("ssfsfsfsfs")
})*/

function f() {
    //var $button = $('.start_plott');
    var $from = $('.from');
    var $to = $('.to');
    var $fun = $('.fun');
    var $degr=$('.degr')
    var $plot = $('.plot')
    var from_val = Number($from.val())
    var to_val = Number($to.val())
    var is_degr=$degr.val()
    if (is_degr){
        from_val=from_val*0.0174
        to_val=to_val*0.0174
    }
    //console.log(to_val - from_val);
    const fun = $fun.val()
    var count=0
    var points=[]
    const step=(to_val-from_val)/100
    for(i=from_val;i<=to_val;i+=step) {
        const x = i;
        points[count]=[];
        points[count].push(x);
        const y = eval(fun);
        points[count].push(y);
         count++;
    }
    //console.log(points)
    $.plot ($plot, [ points ], {});
}

/*$ . post ( '/api/message' , data )
. done ( function (response) {
    console.log(response);
})
. fail( function (error) {
    alert ( 'Failed to create message' );
    console. log (error);
});
*/
//var $from = $(‘.from);
//$button.click(onClick);
//e.preventDefault()
//$from.val()



//const y=eval(fun);
//$. plot ( $ output, [ points ], {});