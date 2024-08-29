import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import axios from 'axios';
import MonitorEquipment from '../MonitorEquipment';
import '@testing-library/jest-dom'

// Mock axios
jest.mock('axios');

describe('MonitorEquipment Component', () => {
  const mockEquipmentList = [
    { id: 1, equipment_type: 'Treadmill' },
    { id: 2, equipment_type: 'Bike' },
  ];

  beforeEach(() => {
    // Reset the mock before each test
    axios.get.mockResolvedValue({ data: mockEquipmentList });
  });

  test('renders the component and fetches equipment list', async () => {
    render(<MonitorEquipment />);

    // Verify the loading and the final rendered state
    expect(screen.getByText('Monitor Equipment')).toBeInTheDocument();

    // Check if the equipment list is populated
    await waitFor(() => {
      mockEquipmentList.forEach(item => {
        expect(screen.getByText(`#${item.id} - ${item.equipment_type}`)).toBeInTheDocument();
      });
    });
  });
});