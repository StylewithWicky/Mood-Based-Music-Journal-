import React from 'react'
import { Formik, Form, Field, ErrorMessage } from 'formik'
import * as Yup from 'yup'
import axios from 'axios'
import '../Css/LoginForm.css'

function LoginForm({ onLogin }) {
  const handleSubmit = async (values, { setSubmitting, setErrors }) => {
    console.log("Form values:", values)  
    try {
      const res = await axios.post('http://localhost:5000/auth/login', values)

      const { token } = res.data
      localStorage.setItem('token', token)
      onLogin()  // ✅ call parent to switch to MoodForm
    } catch (err) {
      setErrors({ general: 'Invalid login credentials' })
    } finally {
      setSubmitting(false)
    }
  }

  return (
<div className="login-container">
  <img src="Frontend/my-app/src/assets/Screenshot from 2025-06-27 23-18-51.png" alt="avatar" />
  <h2>Login Form</h2>
      <Formik
        initialValues={{ email: '', password: '' }}
        validationSchema={Yup.object({
          email: Yup.string().email("Invalid email").required("Required"),
          password: Yup.string().required("Required")
        })}
        onSubmit={handleSubmit}
      >
        {({ isSubmitting, errors }) => (
          <Form>
            <div>
              <label>Email:</label>
              <Field name="email" type="email" />
              <ErrorMessage name="email" component="div" />
            </div>
            <div>
              <label>Password:</label>
              <Field name="password" type="password" />
              <ErrorMessage name="password" component="div" />
            </div>
            {errors.general && <div>{errors.general}</div>}
            <button type="submit" disabled={isSubmitting}>Login</button>
          </Form>
        )}
      </Formik>
    </div>
  )
}

export default LoginForm
