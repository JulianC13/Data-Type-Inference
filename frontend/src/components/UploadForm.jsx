import React, { useState } from "react";
import api from "../api";
import DataTable from "./DataTable"; // Import the DataTable component
import "../styles/uploadForm.css"
import LoadingIndicator from "./LoadingIndicator";


function UploadForm() {
  // State variables for file, response data, error, and loading status
  const [file, setFile] = useState(null);
  const [responseData, setResponseData] = useState(null); 
  const [error, setError] = useState(null); 
  const [loading, setLoading] = useState(false);
  // Function to handle file change event
  const handleFileChange = (event) => {
    console.log(event.target.files[0])
    setFile(event.target.files[0]);
  };

  // Function to handle file upload

  const handleUpload = async (e) => {
    setLoading(true);
    e.preventDefault();
    const formData = new FormData();
    formData.append('file', file);
    if (file == undefined) {
        alert('Please select a file')
       setLoading(false);
    }else{
      setError(null); // Clear previous errors
      // Send the file data to the server
      await api.post("/api/sendData/", formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      .then(response => {
        setResponseData(response.data);
        setLoading(false)
      })
      .catch(error => {
        setLoading(false)
        setError("An error occurred while uploading the file."); // Set error message
        alert("An error occurred on the backend while uploading the file."); // Set error message
      });
    }
   
  };

  return (
    <div className="contanier header-content" >
      <h1>Inference and Conversion Tool</h1>
      <form className="center" onSubmit={handleUpload}>
        <input className="button-file" id="file" type="file" accept=".csv" onChange={handleFileChange} />
        {loading && <LoadingIndicator />}
        <button className="button-file" type="submit">IMPORT CSV</button>
      </form>
       {/* Display the data table if response data is available */}
       {responseData && <DataTable data={responseData} />}
    </div>
  );
}

export default UploadForm;


