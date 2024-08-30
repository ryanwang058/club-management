import React, { useState, useEffect } from 'react';
import axios from 'axios';

const MonitorEquipment = () => {
  const [equipmentList, setEquipmentList] = useState([]);
  const [selectedEquipment, setSelectedEquipment] = useState('');
  const [message, setMessage] = useState('');

  // Function to fetch the initial list of broken equipment
  const fetchBrokenEquipment = () => {
    axios.get('/api/equipment/broken/')
      .then(response => {
        setEquipmentList(response.data);
      })
      .catch(error => {
        console.error("There was an error fetching the equipment list!", error);
      });
  };

  useEffect(() => {
    const socket = new WebSocket('ws://localhost:8000/ws/equipment/');

    fetchBrokenEquipment()

    // Handle messages received from the WebSocket
    socket.onmessage = function(event) {
      const data = JSON.parse(event.data);
      console.log(data)
      
      // If we receive updated broken equipment data
      if (data.broken_equipment) {
        console.log("EquipmentList changed")
      }

      // If an equipment item was fixed
      if (data.fixed_equipment_id) {
        setEquipmentList(prevList => {
          return prevList.filter(equipment => equipment.id !== parseInt(data.fixed_equipment_id));
        });
      }
    };

    // Cleanup function to close WebSocket when the component is unmounted
    return () => {
      socket.close();
    };
  }, []);


  const handleSubmit = (event) => {
    event.preventDefault();
    const equipmentId = selectedEquipment;
    axios.post(`/api/equipment/${equipmentId}/fix/`)
      .then(response => {
        setMessage('Equipment fixed successfully!');
      })
      .catch(error => {
        console.error("There was an error fixing the equipment!", error);
        setMessage('Error fixing equipment.');
      });
  };

  return (
    <div>
      <h2>Monitor Equipment</h2>
      <form onSubmit={handleSubmit}>
        <select 
          value={selectedEquipment} 
          onChange={(e) => setSelectedEquipment(e.target.value)}
        >
          <option value="" disabled>Select broken Equipment to fix</option>
          {equipmentList.map(equipment => (
            <option key={equipment.id} value={equipment.id}>
              #{equipment.id} - {equipment.equipment_type}
            </option>
          ))}
        </select>
        <button type="submit">Fix Selected Equipment</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
};

export default MonitorEquipment;