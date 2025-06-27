import React from 'react'
import { Formik, Form, Field, ErrorMessage } from 'formik'
import * as Yup from 'yup'
import axios from 'axios'

function MoodForm() {
  const handleSubmit = async (values, { resetForm }) => {
    try {
      await axios.post('http://localhost:5000/moods', values, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('token')}`
        }
      })
      resetForm()
    } catch (err) {
      console.error('Error submitting mood:', err)
    }
  }

  return (
    <div>
      <h2>Log Your Mood</h2>
      <Formik
        initialValues={{ mood: '', journal_entry: '', emotion_type_id: '' }}
        validationSchema={Yup.object({
          mood: Yup.string().required('Mood is required'),
          emotion_type_id: Yup.string().required('Emotion is required')
        })}
        onSubmit={handleSubmit}
      >
        {({ isSubmitting }) => (
          <Form>
            <div>
              <label>Mood:</label>
              <Field name="mood" as="select">
                <option value="">Select mood</option>
                <option value="Happy">Happy</option>
                <option value="Sad">Sad</option>
                <option value="Anxious">Anxious</option>
                <option value="Angry">Angry</option>
                <option value="Grateful">Grateful</option>
              </Field>
              <ErrorMessage name="mood" component="div" />
            </div>

            <div>
              <label>Emotion Type:</label>
              <Field name="emotion_type_id" as="select">
                <option value="">Select emotion</option>
                <option value={1}>Happy</option>
                <option value={2}>Sad</option>
                <option value={3}>Angry</option>
                <option value={4}>Anxious</option>
                <option value={5}>Grateful</option>
              </Field>
              <ErrorMessage name="emotion_type_id" component="div" />
            </div>

            <div>
              <label>Journal Entry:</label>
              <Field name="journal_entry" as="textarea" />
            </div>

            <button type="submit" disabled={isSubmitting}>Submit</button>
          </Form>
        )}
      </Formik>
    </div>
  )
}

export default MoodForm
