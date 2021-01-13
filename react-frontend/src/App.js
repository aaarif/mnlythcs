import logo from './logo.svg';
// import Generate from './Generate';
import React, { useState, useEffect } from 'react';
import './App.css';


function App() {
  const [gen,setGen] = useState({});
  return (
    <>
    <Generate/>
    </>
  );
}



function Generate(){
  const [data,setData] = useState({});
  function randomizeFile(){
    fetch('generate')
    .then(response => response.json())
    .then(data =>setData(data));
  }

  const [report,setReport] = useState({});
  function showReport(){
    // alert("report button clickec");
    setReport(data.report);

  }
  console.log("This is data from API generate ",data);
  return(
    <>
    <button onClick = {randomizeFile}>Generate</button>
    <p>
    <a href="/download">Download Link to file:{data.file }</a>
    </p>
    <p></p>
    <button onClick = {showReport}>Report</button>
     <p>Alphabetical String: {report.strnum}</p>
     <p>Real Numbers: {report.realnum} </p>
     <p>Integer:  {report.intgr}</p>
     <p>Alphanumeric:  {report.alphanum}</p>
    </>
  )
}


export default App;




