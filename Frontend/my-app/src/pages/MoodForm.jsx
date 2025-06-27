import React, { useState } from 'react';
import { Formik, Form, Field } from 'formik';
import axios from 'axios';
import SongCard from '../components/SongCard';
import '../Css/MoodForm.css';

function MoodForm() {
  const [songData, setSongData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [errorMsg, setErrorMsg] = useState('');

  const handleSubmit = async (values, { resetForm }) => {
    setLoading(true);
    setSongData(null);
    setErrorMsg('');

    const payload = {
      mood: values.mood,
      journal_entry: values.journal_entry,
      user_id: 1, // 🔁 Replace with actual user ID after login
      emotion_type_id: 1, // 🔁 Link to proper emotion ID
    };

    try {
      await axios.post('http://localhost:5000/moods', payload);
      const res = await axios.get(
        `http://localhost:5000/recommendation?mood=${values.mood}`
      );
      setSongData(res.data);
      resetForm();
    } catch (err) {
      console.error(err);
      setErrorMsg('Could not fetch song recommendation.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      {/* Header */}
      <div className="form-header">
        <h2 className="form-title">🎭 How Are You Feeling Today?</h2>
        <button
          onClick={() => {
            localStorage.removeItem('token');
            window.location.reload();
          }}
          className="logout-btn"
        >
          Logout
        </button>
      </div>

      {/* Main Form + Calendar */}
      <div className="calm">
        {/* Form Container */}
        <div className="form-container">
          <Formik
            initialValues={{ mood: '', journal_entry: '' }}
            onSubmit={handleSubmit}
          >
            <Form className="space-y-4 glass-form">
              <div>
                <label htmlFor="mood" className="block text-sm font-medium text-gray-700">
                  Mood
                </label>
                <Field
                  as="select"
                  name="mood"
                  className="mt-1 block w-full border border-gray-300 rounded-md p-2"
                  required
                >
                  <option value="">Select a mood</option>
                  <option value="Happy">Happy</option>
                  <option value="Sad">Sad</option>
                  <option value="Angry">Angry</option>
                  <option value="Anxious">Anxious</option>
                  <option value="Grateful">Grateful</option>
                </Field>
              </div>

              <div>
                <label htmlFor="journal_entry" className="block text-sm font-medium text-gray-700">
                  Journal Entry
                </label>
                <Field
                  as="textarea"
                  name="journal_entry"
                  rows="4"
                  className="mt-1 block w-full border border-gray-300 rounded-md p-2"
                  placeholder="Write a short reflection..."
                  required
                />
              </div>

              <button
                type="submit"
                disabled={loading}
                className="w-full bg-indigo-600 hover:bg-indigo-700 text-white py-2 rounded-md font-semibold"
              >
                {loading ? 'Submitting...' : 'Log Mood & Get Song 🎵'}
              </button>
            </Form>
          </Formik>

          {errorMsg && (
            <p className="text-red-500 text-center mt-4">{errorMsg}</p>
          )}

          {songData && (
            <SongCard
              song={songData.song}
              artist={songData.artist}
              url={songData.url}
              previewUrl={songData.preview_url}
              cover={songData.cover_art} // if available
            />
          )}
        </div>

        {/* Calendar */}
        <div className="calendar-box">
          <h3>Select a Date</h3>
          <input type="date" className="calendar-input" />
        </div>
      </div>
    </div>
  );
}

export default MoodForm;
