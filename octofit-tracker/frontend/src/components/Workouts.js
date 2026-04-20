import React, { useEffect, useState } from 'react';

const difficultyBadge = (difficulty) => {
  const map = { easy: 'success', medium: 'warning', hard: 'danger' };
  const color = map[(difficulty || '').toLowerCase()] || 'secondary';
  return <span className={`badge bg-${color}`}>{difficulty}</span>;
};

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);
  const endpoint = `${process.env.REACT_APP_CODESPACE_NAME ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/` : '/api/workouts/'}`;

  useEffect(() => {
    console.log('Fetching Workouts from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = Array.isArray(data) ? data : data.results || [];
        setWorkouts(results);
        console.log('Fetched Workouts:', data);
      })
      .catch(err => console.error('Error fetching workouts:', err));
  }, [endpoint]);

  return (
    <div className="card octofit-card mb-4">
      <div className="card-header">&#128170; Workouts</div>
      <div className="card-body p-0">
        <table className="table table-striped table-hover mb-0">
          <thead>
            <tr>
              <th>#</th>
              <th>Name</th>
              <th>Difficulty</th>
            </tr>
          </thead>
          <tbody>
            {workouts.length === 0 ? (
              <tr><td colSpan="3" className="text-center text-muted py-3">No workouts found.</td></tr>
            ) : (
              workouts.map((workout, idx) => (
                <tr key={workout._id || workout.id || idx}>
                  <td>{idx + 1}</td>
                  <td><strong>{workout.name}</strong></td>
                  <td>{difficultyBadge(workout.difficulty)}</td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Workouts;
