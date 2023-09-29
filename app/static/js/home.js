let pw1=document.getElementById('pw1');
let signup=document.getElementById('signupbtn');
// let pw2=document.getElementById('pw2');
let pw2=document.getElementById('pw2').addEventListener("change",displaypwerr);
let contactno=document.getElementById('contactno').addEventListener('change',displaynumerr);
function displaypwerr(){
  let pw1=document.getElementById('pw1');
   pw2=document.getElementById('pw2');
  let pwerr=document.getElementById('pwerr')
  let numvalid=true
 let pwvalid=true
  // signup.classList.add('invisible');
   if(pw1.value != pw2.value){
    pwerr.classList.remove("invisible");  
    signup.classList.add('mute');
    pwvalid=false
    // signup.style.pointerEvents='none';
   }
   if(pw1.value == pw2.value && numvalid && pwvalid){
    pwerr.classList.add("invisible");  
    signup.classList.remove('mute');
    pwvalid=true
   }
}

function displaynumerr(){
  let numerr=document.getElementById('numerr')
  contactno=document.getElementById('contactno');
if(contactno.value > 9999999999 || contactno.value < 1111111111){
  numerr.classList.remove("invisible");  
  signup.classList.add('mute');
  console.log(contactno.value)
  numvalid=false
}

else{
  valid=true
  numerr.classList.add("invisible");  
  signup.classList.remove('mute');
}

}


