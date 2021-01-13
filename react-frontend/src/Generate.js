import React, { Component } from 'react';

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

class Generate extends Component{
    constructor(props){
        super(props);
        this.state={
            filename:""
        }
    }
    parentFunction=(data_from_child)=>{
        fetch('/generate')
        .then(response => response.json())
        .then(data =>setData(data));
        this.setState({value_key:data_from_child});
    }
    randomizeFile(e) {
        fetch('/generate')
        .then(response => response.json())
        .then(data =>setData(data));
    }
    render(){
        return(
            <>
    <button onClick = {this.randomizeFile}>Generate</button>
    <p>
    <a href="">Download Link to file:{ data.file }</a>
    </p>
    </>
        );
    }
}
export default Generate;