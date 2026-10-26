-- Demo data: 8 categories, ~40 transactions across Aug–Oct 2026
-- Run: psql budget_tracker < seed.sql

INSERT INTO categories (name, color) VALUES
    ('Groceries', '#4caf50'),
    ('Dining out', '#ff9800'),
    ('Transport', '#2196f3'),
    ('Rent', '#9c27b0'),
    ('Utilities', '#607d8b'),
    ('Entertainment', '#e91e63'),
    ('Health', '#00bcd4'),
    ('Other', '#9e9e9e')
ON CONFLICT (name) DO NOTHING;

-- TODO(Session 3): add ~40 INSERTs for transactions spread across
-- 2026-08, 2026-09, 2026-10 so the monthly summary view has real data.
-- Example:
-- INSERT INTO transactions (amount, date, note, category_id) VALUES
--     (64.20, '2026-10-03', 'Ralphs weekly shop',
--      (SELECT id FROM categories WHERE name = 'Groceries'));
