import React, { useState, useEffect } from 'react';
import axios from 'axios';

const MonitorEquipment = () => {
  const [equipmentList, setEquipmentList] = useState([]);
  const [selectedEquipment, setSelectedEquipment] = useState('');
  const [message, setMessage] = useState('');

  useEffect(() => {
    // Fetch the list of broken equipment from the backend
    axios.get('/api/equipment/broken/')
      .then(response => {
        setEquipmentList(response.data);
      })
      .catch(error => {
        console.error("There was an error fetching the equipment list!", error);
      });
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