using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Support.UI;
using System;

class NavigateToInvu
{
    static void Main()
    {
        // 1. ბრაუზერის დაწყება
        IWebDriver driver = new ChromeDriver();

        try
        {
            // 2. გადადით INVU.GE გვერდზე
            driver.Navigate().GoToUrl("https://invu.ge");

            // 3. ელოდება, რომ გვერდი ჩაიტვირთოს (მარტივი გზა)
            WebDriverWait wait = new WebDriverWait(driver, TimeSpan.FromSeconds(10));
            wait.Until(d
