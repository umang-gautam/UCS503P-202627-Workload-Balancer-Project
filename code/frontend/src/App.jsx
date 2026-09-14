import { Routes, Route } from 'react-router-dom'
import { StudentProvider } from './context/StudentContext.jsx'
import Layout from './components/Layout.jsx'
import Dashboard from './pages/Dashboard'
import Students from './pages/Students'
import Subjects from './pages/Subjects'
import PerformanceEntry from './pages/PerformanceEntry'
import StudyPlanView from './pages/StudyPlanView'

export default function App() {
  return (
    <StudentProvider>
      <Layout>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/students" element={<Students />} />
          <Route path="/subjects" element={<Subjects />} />
          <Route path="/scores" element={<PerformanceEntry />} />
          <Route path="/performance" element={<PerformanceEntry />} />
          <Route path="/study-plan" element={<StudyPlanView />} />
        </Routes>
      </Layout>
    </StudentProvider>
  )
}
