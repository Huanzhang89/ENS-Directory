import React, { Component } from 'react'

const Owner = props => {
  return (
    <div className="labels">
      <div className="label">{props.ownerData[0]}</div>
      <div className="label">{props.ownerData[1]}</div>
    </div>
  )
}

export default Owner
