import React from 'react'
import Owner from './Owner'

const Owners = props => {
  return (
    <div className="owner-list-container">
      <div className="labels">
        <div className="label bold">From Block</div>
        <div className="label bold">Owned By</div>
      </div>
      {props.ownerHistory.map(owner => (
        <Owner key={owner.block} ownerData={owner} />
      ))}
    </div>
  )
}

export default Owners
