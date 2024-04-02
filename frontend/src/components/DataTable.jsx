import { useState } from "react";
import "../styles/dataTable.css"
import { CSVLink, CSVDownload } from "react-csv";
function DataTable({ data }) {
  const dataTypeMappings = {
    'object': 'Text',
    'int64': 'Integer',
    'float64': 'Float',
    'bool': 'Boolean',
    'datetime64[ns]': 'Date',
    'category': 'Cat',
    // Add more mappings as needed
  };
  const [customDataTypes, setCustomDataTypes] = useState({});

  const handleDataTypeChange = (columnName, dataType) => {
    setCustomDataTypes({
      ...customDataTypes,
      [columnName]: dataType,
    });
  };
  // console.log(data.data)
    if (!data.data || data.data.length === 0) {
      return <div>No data available</div>; // Display a message if data is empty or null
    }
    return (
    <div>
      <h2>Data Table</h2>
      <CSVLink
            style={{ textDecoration: 'none' }}
            data={data.data}
            // I also tried adding the onClick event on the link itself
            filename={'my-file.csv'}
            target="_blank"
        >
              Download me
        </CSVLink> 
      <table className="table table-striped">
        <thead>
          <tr>
            {Object.keys(data.data[0]).map((key) => (
              <th key={key}>
                {key} <br></br>
                <select
                  value={customDataTypes[key] || data.types[key]}
                  onChange={(e) => handleDataTypeChange(key, e.target.value)}
                >
                  {Object.keys(dataTypeMappings).map((dataType) => (
                    <option key={dataType} value={dataType}>
                      {dataTypeMappings[dataType]}
                    </option>
                  ))}
                </select>
                
              </th>
            ))}

           
          </tr>
        </thead>
        <tbody>
          {data.data.map((row, index) => (
            <tr key={index}>
              {Object.values(row).map((value, index) => (
                <td key={index}>{value}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
     );
}

export default DataTable;
