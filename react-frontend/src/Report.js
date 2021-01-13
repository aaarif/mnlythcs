import React, { Component } from 'react'

export function Report({rep}){
    function showReport(){
            alert('Thanks for clicking report');
        
          }
   return (
    <>
    <button onClick = {showReport}>Report</button>
    <p>Alphabetical String:</p>
    <p>Real Numbers:</p>
    <p>Integer:</p>
    <p>Alphanumeric:</p>
   </>
   ) 
}
export default Report;