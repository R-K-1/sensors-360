import React from 'react';

class Dashboard extends React.Component{
  state = {
    heartbeats: []
  }
  componentDidMount() {
    var ws = new WebSocket('ws://localhost:6000/')

    ws.onopen = () => {
      // on connecting, do nothing but log it to the console
      console.log('connected')
    }

    ws.onmessage = evt => {
      // listen to data sent from the websocket server
      const message = JSON.parse(evt.data)
      this.setState({heartbeats: message})
      console.log(message)
    }

    ws.onclose = () => {
      console.log('disconnected')
      // automatically try to reconnect on connection loss

    }
  }

  render() {

      return (
          <div>
          </div>
      )
  }

}

export default Dashboard;
