/*
File: UserTable.js

Description:
This file implements the main user table component which displays all the users
currently synced from slack. It uses the reactstrap table. It fetches data from the
flask API.

*/

import React from 'react';
import { Table, Button } from 'reactstrap';

let APIURL = process.env.REACT_APP_API_URL + 'activeUsers/' 

function fetchUsers() {
  fetch(APIURL)
    .then(response => response.json())
    .then(data => {
      console.log("success")
      console.log(data);
      return data;
    })
    .catch(error => {
      console.log("there was an error fetching users: ", error);
      return;
    });
}

function fetchUpdate() {
  return
}

class UserTable extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      users: [],
    };
  }

  componentDidMount() {
    fetch(APIURL)
      .then(response => response.json())
      .then(resData => {
        console.log("success")
        console.log(resData);
        this.setState({
          users: resData['users'],
          isLoaded: true
        });
        },
        (error) => {
          this.setState({
            isLoaded: true,
            error
          });
        }
      )
  }

  getType(userData) {
    if (userData.is_admin) {
      return 'admin'
    } else if(userData.is_bot) {
      return 'bot'
    } else {
      return 'member'
    }
  }

  render() {
    const error = this.state.error;
    const usrData = this.state.users;
    const isLoaded = this.state.isLoaded;
    console.log("data", usrData)
    if(error) {
      return (
        <div>Error Fetching</div>
      )
    } else if (!isLoaded) {
      return (
        <div>Loading...</div>
      )
    } else {
      return (
        <div>
          <Table id="UserTable" dark responsive>
            <thead>
              <tr>
                <th></th>
                <th>id</th>
                <th>Full Name</th>
                <th>Username</th>
                <th>Role</th>
                <th>Deleted</th>
              </tr>
            </thead>
            <tbody>
              {usrData.map(user => (
                <tr key={user.id+'user'}>
                  <td key={user.id + 'img'}><img src={user.profile.image_32}/></td>
                  <td key={user.id} scope="row">{user.id}</td>
                  <td key={user.id + 'real_name'}>{user.real_name}</td>
                  <td key={user.id + 'name'}>{user.name}</td>
                  <td key={user.id + 'type'}>{this.getType(user)}</td>
                  <td key={user.id + 'deleted'}>{user.deleted ? 'true' : 'false'}</td>
                  </tr>
              ))}
            </tbody>
          </Table>
        </div>
      );
    }
  }
}

export default UserTable;