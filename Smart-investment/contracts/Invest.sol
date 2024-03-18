// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import ChainlinkClient from the Chainlink library
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract Invest {

    AggregatorV3Interface internal priceFeed;

    address payable public recipient;

     constructor(address _recipient, address _priceFeedAddress) {
        recipient = payable(_recipient);
        priceFeed = AggregatorV3Interface(_priceFeedAddress);
    }

    function collectAndTransfer() public payable {
        // Define the amount in USD that you want to transfer
        uint256 amountUSD = 20; // $20 worth of Ether

        // Fetch latest ETH/USD price from Chainlink Oracle
        (, int256 price, , , ) = priceFeed.latestRoundData();

        // Calculate the equivalent amount in wei based on the current ETH/USD price
        uint256 amountWei = (amountUSD * 1 ether) / uint256(price);

        // Ensure that the sender has sent enough wei
        require(msg.value >= amountWei, "Insufficient amount sent");

        // Transfer Ether to the recipient
        payable(recipient).transfer(amountWei);
    }

    function getBalance(address _address) public view returns(uint) {
        return _address.balance;
    }
}
