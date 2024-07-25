function addreview() {
    var reviewbutton = document.getElementById('newreview');

    var display = reviewbutton.style.display;

    if(display == 'block'){
        reviewbutton.style.display = 'none';      
    }
    else{
        reviewbutton.style.display = 'block';
    }
    
}