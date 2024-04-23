import { BrowserRouter, Route, Routes } from 'react-router-dom'
import './App.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import Login from './components/login'
import {store} from './redux/store'
import { Provider } from 'react-redux'
import Dashboard from './components/dashboard'
import Producer from './components/producer'
import Farms from './components/farms'
import Areas from './components/areas'
import Menu from './components/misc/navbar'


function App() {

  return (
    <>
    <Menu></Menu>
    <Provider store={store}>
      <BrowserRouter>
        <Routes>
          <Route path="/" Component={Login} />
          <Route path="/dashboard" Component={Dashboard} />
          <Route path="/producer" Component={Producer} />
          <Route path="/farm" Component={Farms} />
          <Route path="/area" Component={Areas} />
        </Routes>
      </BrowserRouter>
    </Provider>
    </>
  )
}

export default App


