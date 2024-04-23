const { Builder, By } = require('selenium-webdriver');
const fs = require('fs');

const driver = new Builder()
    .forBrowser('MicrosoftEdge')
    .build();

async function test(url) {
    const logFilePath = 'test.txt';
    if (fs.existsSync(logFilePath)) {
        fs.unlinkSync(logFilePath);
    }
    const logStream = fs.createWriteStream(logFilePath, { flags: 'a' });
    try {
        logStream.write('Open page: ' + url + '\n');

        await driver.get(url);

        const email = 'ivan@mail.ru';
        const password = 'bhewrtfm3klmt3';

        logStream.write('Input email: ' + email + '\n');
        await driver.findElement(By.id("input-0")).sendKeys(email);

        logStream.write('Input password: ' + password + '\n');
        await driver.findElement(By.id("input-2")).sendKeys(password);

        logStream.write('Click on sign in button\n');
        await driver.findElement(By.id('sign-in-button')).click();
        await driver.sleep(100)

        const currentUrl = await driver.getCurrentUrl();
        if (currentUrl === 'http://localhost:8081/e.moevm.statistics/statistics') {
            logStream.write('SUCCESS! Sign in was success\n');
        }
        else {
            logStream.write('ERROR! Catch error then sign in\n');
        }
    } finally {
        logStream.write('Exit browser\n');
        await driver.quit();
        logStream.end();
    }
}

test('http://localhost:8081/');
