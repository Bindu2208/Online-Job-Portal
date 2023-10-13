function addNewWeField()
{
   let newNode=document.createElement('textarea');
      newNode.classList.add('form-control');
        newNode.classList.add('weField');
        newNode.classList.add('mt-2');
        newNode.setAttribute("rows",3);
        newNode.setAttribute("placeholder","Enter here");
        let weOb=document.getElementById("we");
        let weAddButtonOb=document.getElementById("weAddButton");
        weOb.insertBefore(newNode,weAddButtonOb);


}
function addNewAQField()
{
   let newNode=document.createElement('textarea');
      newNode.classList.add('form-control');
        newNode.classList.add('eqField');
        newNode.classList.add('mt-2');
        newNode.setAttribute("rows",3);
        newNode.setAttribute("placeholder","Enter here");
        let aqOb=document.getElementById("aq");
        let aqAddButtonOb=document.getElementById("aqAddButton");
        aqOb.insertBefore(newNode,aqAddButtonOb);
}



function generateCV()
{
    // let nameField=document.write(document.getElementById("nameField").value);
    // let nameT1=document.getElementById("nameT1");
    // nameT1.innerHTML=nameField;

    let nameField=document.getElementById("nameField").value;
    let nameT1=document.getElementById("nameT1");
    nameT1.innerHTML=nameField;

    // document.getElementById("contactT").innerHTML=document.getElementById("contactField").value;

    document.getElementById("nameT2").innerHTML=nameField;

    document.getElementById("contactT").innerHTML=document.getElementById("contactField").value;

    document.getElementById("addressT").innerHTML=document.getElementById("addressField").value;

    document.getElementById("fbT").innerHTML=document.getElementById("fbField").value;

    document.getElementById("instaT").innerHTML=document.getElementById("instaField").value;


    document.getElementById("linkedT").innerHTML=document.getElementById("linkedField").value;

    document.getElementById("objectiveT").innerHTML=document.getElementById("objective").value;

    // let wes=document.getElementsByClassName("we");
    // let str="";
    // for(let e of wes)
    // {
    //     str=str+`<li>${e.value}</li>`;
    // }
    // document.getElementById("weT").innerHTML=str;
    // let aqs=document.getElementsByClassName("aq");
    // let str1="";
    // for(let e of aqs)
    // {
    //     str1=str1+`<li>${e.value}</li>`;
    // }
    // document.getElementById("aqT").innerHTML=str1;

    document.getElementById("weT").innerHTML=document.getElementById("we").value;
    document.getElementById("aqT").innerHTML=document.getElementById("aq").value;
    document.getElementById("cv-form").style.display="none";
    document.getElementById("cv-template").style.display="block";


}

function printCV()
{
    window.print();
}