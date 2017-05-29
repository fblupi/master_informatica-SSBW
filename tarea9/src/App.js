import React, { Component } from "react";
import "./App.css";
import "bootswatch/simplex/bootstrap.css";

import { Navbar, NavItem, Nav, Grid, Row, Col } from "react-bootstrap";

const ALBUMS = [
  { name: "Aunque esté mal contarlo", albumID: "7cJ6v0KvM1TocA5ID0FgDu" },
  { name: "La Vida Plena", albumID: "0ji205YLsJO7V4tJVl0lEk" },
  { name: "Sólo los locos viven la libertad", albumID: "0CEajBz3mowiDuyFiWHy5S" },
  { name: "SoloLuna", albumID: "4AxfGdW8dMFm9ogSfpdBWh" }
];

class AlbumDisplay extends Component {
  constructor() {
    super();
    this.state = {
      albumData: null
    };
  }
  componentDidMount() {
    const token = "Bearer BQDdS3PtZ6pEkeEzsuzJTJnnu_NdxcG9G4c2f3NWM-xNTwIjsD0pNz3BmuIWL737vCL-5Z1sX1KIyc5siVVBk2P48HGSgCf0McAv0JXWfhjDXrWt9xxRod5UAPnZFJyC9NUyrLZ7B7HqdBy12nz6t-F1Uye5xmWgIDV7ptJGFpTKKmO_9jTc2iJF7DCqX1ad2xrun4hA7Sd6vyCFroWORt0Lvj1IS284w4Zf4QgGiO8scvxJQAuPopr89y_RjJblVyD-T5prU3Jw4cx6KrHCrA3t2KRSwQ84bdtUsZTKF8wor944uDJbK9x-_17ErA";
    const albumID = this.props.albumID;
    const albumURL = "https://api.spotify.com/v1/albums/" + albumID;
    const tracksURL = "https://api.spotify.com/v1/albums/" + albumID + "/tracks";
    fetch(albumURL, {
      method: "GET",
      headers: {
        "Accept": "application/json",
        "Authorization": token
      }
    }).then(res => res.json()).then(json => {
      this.setState({ albumData: json });
    });
    fetch(tracksURL, {
      method: "GET",
      headers: {
        "Accept": "application/json",
        "Authorization": token
      }
    }).then(res => res.json()).then(json => {
      this.setState({ songsData: json });
    });
  }
  render() {
    const songsData = this.state.songsData;
    const albumData = this.state.albumData;
    if (!albumData) return <div>Cargando...</div>;

    const title = albumData.name;

    const albumImg = albumData.images[0].url;

    var artists = albumData.artists[0].name;
    for (var i = 1; i < albumData.artists.length; i++) {
      artists += ", ";
      artists += albumData.artists[i].name;
    }

    var songs = [];
    for (var i = 0; i < songsData.items.length; i++) {
      songs.push(<li><a target="_blank" href={songsData.items[i].preview_url}>{songsData.items[i].name}</a></li>);
    }

    return (
      <div>
        <h3>{title}</h3>
        <h5>{artists}</h5>
        <hr/>
        <Row>
          <Col md={4} sm={4}>
            <img src={albumImg} className="album-cover" alt="Cover {title}"/>
          </Col>
          <Col md={6} sm={6}>
            <ol>
              {songs}
            </ol>
          </Col>
        </Row>
      </div>
    );
  }
}

class App extends Component {
  constructor() {
    super();
    this.state = {
      activeAlbum: 0
    };
  }
  render() {
    const activeAlbum = this.state.activeAlbum;
    return (
      <div>
        <Navbar>
          <Navbar.Header>
            <Navbar.Brand>Discografía de Pedro Pastor</Navbar.Brand>
          </Navbar.Header>
        </Navbar>
        <Grid>
          <Row>
            <Col md={4} sm={4}>
              <Nav
                bsStyle="pills"
                stacked
                activeKey={activeAlbum}
                onSelect={index => {
                  this.setState({ activeAlbum: index });
                }}
              >
                {ALBUMS.map((album, index) => (
                  <NavItem key={index} eventKey={index}>{album.name}</NavItem>
                ))}
              </Nav>
            </Col>
            <Col md={8} sm={8}>
              <AlbumDisplay key={activeAlbum} albumID={ALBUMS[activeAlbum].albumID} />
            </Col>
          </Row>
        </Grid>
      </div>
    );
  }
}

export default App;
