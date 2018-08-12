import React, { Component } from 'react'

const Owner = props => {
  return (
    <div className="labels">
      <div className="label">{props.ownerData.block}</div>
      <div className="label">{props.ownerData.owner}</div>
    </div>
  )
}

export default Owner
