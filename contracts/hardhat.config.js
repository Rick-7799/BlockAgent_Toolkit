require('dotenv').config();
require('@nomicfoundation/hardhat-toolbox');

const { CELO_RPC, AURORA_RPC, HARMONY_RPC, PRIVATE_KEY } = process.env;

module.exports = {
  solidity: "0.8.20",
  networks: {
    celoTest: {
      url: CELO_RPC || "https://alfajores-forno.celo-testnet.org",
      accounts: PRIVATE_KEY ? [PRIVATE_KEY] : []
    },
    auroraTest: {
      url: AURORA_RPC || "https://testnet.aurora.dev",
      accounts: PRIVATE_KEY ? [PRIVATE_KEY] : []
    },
    harmonyTest: {
      url: HARMONY_RPC || "https://api.s0.b.hmny.io",
      accounts: PRIVATE_KEY ? [PRIVATE_KEY] : []
    }
  }
};
