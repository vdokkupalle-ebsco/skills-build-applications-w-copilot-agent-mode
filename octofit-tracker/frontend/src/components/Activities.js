import React, { useEffect, useState } from 'react';

const Activities = () => {
  const [activities, setActivities] = useState([]);
  const endpoint = `${process.env.REACT_APP_CODESPACE_NAME ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/` : '/api/activities/'}`;

  useEffect(() => {
    console.log('Fetching Activities from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = Array.isArray(data) ? data : data.results || [];
        setActivities(results);
        console.log('Fetched Activities:', data);
      })
      .catch(err => console.error('Error fetching activities:', err));
  }, [endpoint]);

  return (
    <div className="card octofit-card mb-4">
      <div className="card-header">&#127939; Activities</div>
      <div className="card-body p-0">
        <table className="table table-striped table-hover mb-0">
          <thead>
            <tr>
              <th>#</th>
              <th>User</th>
              <th>Activity</th>
              <th>Duration (min)</th>
            </tr>
          </thead>
          <tbody>
            {activities.length === 0 ? (
              <tr><td colSpan="4" className="text-center text-muted py-3">No activities found.</td></tr>
            ) : (
              activities.map((activity, idx) => (
                <tr key={activity._id || activity.id || idx}>
                  <td>{idx + 1}</td>
                  <td>{activity.user}</td>
                  <td>{activity.activity}</td>
                  <td>{activity.duration}</td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Activities;
