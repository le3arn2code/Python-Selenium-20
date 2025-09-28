const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
    const browser = await puppeteer.launch({
        headless: true,
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    const page = await browser.newPage();
    const filePath = `file:${path.join(__dirname, 'index.html')}`;

    await page.goto(filePath);

    // Select a radio button
    await page.click('input[name="fruit"][value="banana"]');
    console.log('Selected radio: Banana');

    // Select multiple checkboxes
    await page.click('input[name="hobbies"][value="reading"]');
    await page.click('input[name="hobbies"][value="travelling"]');
    console.log('Selected checkboxes: Reading, Travelling');

    // Gather selected inputs
    const selectedInputs = await page.evaluate(() => {
        const inputs = Array.from(document.querySelectorAll('input[type="radio"], input[type="checkbox"]'));
        return inputs
            .filter(input => input.checked)
            .map(input => `${input.type}-${input.value}`);
    });

    console.log('Selected values:', selectedInputs.join(', '));

    await browser.close();
})();
