# SplitShare
SplitShare is an open-source project designed to enable fair division of expenses among group members. It serves as a useful tool for managing shared costs in various scenarios, such as group meals or team outings. With SplitShare, individuals can easily calculate and distribute expenses among themselves, ensuring a fair and transparent process.

The main objective of SplitShare is to streamline the management of shared expenses and simplify the task of tracking individual contributions. It offers a user-friendly interface that allows users to input expenses, specify the participants involved, and automatically calculate each person's share. This eliminates the need for manual calculations and minimizes the potential for errors or misunderstandings.

Whether it's a casual gathering with friends or a more formal setting within a company, SplitShare provides a convenient solution for dividing costs and keeping everyone accountable. By facilitating fair and efficient expense sharing, SplitShare promotes transparency, eliminates financial burdens on a single individual, and enhances the overall experience of group activities.


## Database Structure

### Tables

#### `User` Table

- `id`: Unique identifier for each user.
- `name`: User's name.
- `email`: User's email.
- `google_id`: Unique identifier for the user from Google service (for Gmail login).

#### `Group` Table

- `id`: Unique identifier for each group.
- `name`: Group name.
- `creator_id`: Unique identifier for the user who created the group.
- `default_currency`: Default currency for the group.
- `default_calendar_type`: Default calendar type for the group (Shamsi or Gregorian).
- `invite_link`: Invitation link for joining the group.
- `invite_expiry`: Expiry date and time for the invitation link (one hour).

#### `GroupMember` Table

- `id`: Unique identifier for each group member.
- `group_id`: Unique identifier for the respective group.
- `user_id`: Unique identifier for the user associated with the group membership.

#### `Order` Table

- `id`: Unique identifier for each order.
- `title`: Order title.
- `description`: Order description.
- `group_id`: Unique identifier for the respective group.
- `creator_id`: Unique identifier for the user who created the order.
- `total_amount`: Total amount of the order.

#### `OrderMember` Table

- `id`: Unique identifier for each order member.
- `order_id`: Unique identifier for the respective order.
- `user_id`: Unique identifier for the respective user.
- `amount`: Amount owed by the user for the order.
- `settled_amount`: Amount settled by the user for the order.

#### `Transaction` Table

- `id`: Unique identifier for each transaction.
- `payer_id`: Unique identifier for the user who made the payment.
- `receiver_id`: Unique identifier for the user who received the payment.
- `amount`: Amount of the transaction.
- `order_member_id`: Unique identifier for the respective order member.
- `paid_at`: Date and time of the payment.

This is the complete list of tables required for the SplitShare project database. Please include this information along with the system functionality description in the Markdown format for the project's README on GitHub.

The workflow is as follows:

1. A user logs in through Google login.
2. In the first step, they create a group.
3. In the group, they can add other members either through invitation links or by adding their email.
4. Members of the group can add expenses, e.g., "I bought breakfast today for 50,000 Toman," and the expenses are divided among certain group members (e.g., me and Ali).
5. Now, I can see on my dashboard that Ali owes me 25,000 Toman, and Ali can see on his dashboard that he owes me 25,000 Toman.
6. When the payment is settled, either I or Ali can record that the amount has been settled.
7. It is also possible to aggregate the expenses and settle them, for example, once a month.

Note that this app is multilingual, and the currency unit is different in Iran (Toman) compared to other countries. My suggestion is to specify the group's currency unit and the type of calendar (Shamsi or Gregorian) when creating the group.

The relationship between the tables is as follows:

When a new expense is recorded, an `order` record is created, specifying what was purchased, the description, the total amount, and the creator. At the same time, an `order_member` record is created for each member involved in the expense, including the amount they owe. To determine to whom payment should be made, we refer to the `order` table and its `creator_id` field.

When the payment is made, we can view the list of members in the order, select multiple members, and mark their payment as settled. Then, a `transaction` is recorded, indicating who made the payment, who received the payment, the amount of the payment, and the respective `order_member` record. In the `order_member` table, we update the `settled_amount` field to indicate that the user is no longer in debt and has made the payment.
