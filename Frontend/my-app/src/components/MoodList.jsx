import React, { useEffect, useState } from 'react'
import axios from 'axios'

function MoodList() {
  const [logs, setLogs] = useState([])

  useEffect(() => {
    axios.get('http://localhost:5000/moods', {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`
      }
    })
      .then(res => setLogs(res.data))
      .catch(err => console.error(err))
  }, [])

  return (
    <div>
      <h3>Previous Mood Logs</h3>
      <ul>
        {logs.map(log => (
          <li key={log.id}>
            <strong>{log.mood}</strong>: {log.journal_entry} ({new Date(log.created_at).toLocaleString()})
          </li>
        ))}
      </ul>
    </div>
  )
}

export default MoodList
