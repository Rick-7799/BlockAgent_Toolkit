const hre = require('hardhat')

async function main() {
  const SimpleStorage = await hre.ethers.getContractFactory('SimpleStorage')
  const storage = await SimpleStorage.deploy()
  await storage.deployed()
  console.log('SimpleStorage deployed to:', storage.address)
}

main().catch((error) => {
  console.error(error)
  process.exitCode = 1
})
