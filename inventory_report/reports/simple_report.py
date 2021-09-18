import datetime


class SimpleReport:
    @staticmethod
    def check_expired_product(product):
        product_date = datetime.datetime.strptime(product, "%Y-%m-%d").date()
        today_date = datetime.date.today()

        if today_date > product_date:
            return None

        days_to_expire = product_date - today_date
        return days_to_expire.days

    @staticmethod
    def older_fabrication(actual_fab, new_fab):
        actual_fab_date = datetime.datetime.strptime(
            actual_fab, "%Y-%m-%d"
        ).date()

        new_fab_date = datetime.datetime.strptime(new_fab, "%Y-%m-%d").date()
        if new_fab_date < actual_fab_date:
            return new_fab
        return actual_fab

    @staticmethod
    def format_output(fabrication, expiration, company):
        formatted_str = (
            "Data de fabricação mais antiga: " + fabrication + "\n"
        )
        formatted_str += "Data de validade mais próxima: " + expiration + "\n"
        formatted_str += (
            "Empresa com maior quantidade" +
            " de produtos estocados: " + company + "\n"
        )

        return formatted_str

    @staticmethod
    def most_prod_company(companies):
        products = -1
        company = ""
        for key in companies:
            if companies[key] > products:
                products = companies[key]
                company = key
        return company

    @staticmethod
    def generate(data: list()):
        if len(data) == 0:
            return ""

        companies = dict()
        older_fab = data[0]["data_de_fabricacao"]
        close_exp_date = data[0]["data_de_validade"]
        close_exp_days = SimpleReport.check_expired_product(close_exp_date)

        for d in data:
            older_fab = SimpleReport.older_fabrication(
                older_fab, d["data_de_fabricacao"]
            )
            exp_date = d["data_de_validade"]
            exp_days = SimpleReport.check_expired_product(exp_date)

            if (exp_days is not None) and (exp_days < close_exp_days):
                close_exp_days = exp_days
                close_exp_date = exp_date

            company = d["nome_da_empresa"]
            companies[company] = companies[company] + 1 \
                if company in companies else 1

        most_prod_company = SimpleReport.most_prod_company(companies)
        return SimpleReport.format_output(
            older_fab, close_exp_date, most_prod_company
        )
